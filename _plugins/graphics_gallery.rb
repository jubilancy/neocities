# ---------------------------------------------------------------------------
# graphics_gallery.rb
#
# Scans graphics/<folder>/ at build time and, for every folder that contains
# at least one image, generates a page at /graphics/<folder>/.
#
# You never touch config to add a category. Make a folder, drop images in,
# push. The folder shows up on /graphics/ and gets its own page.
#
# Display names + blurbs are OPTIONAL. If _data/graphics.yml has an entry
# keyed by folder name it wins; otherwise the folder name is humanised.
#
# This runs because the site is built by GitHub Actions. It would NOT run on
# GitHub Pages, which only allows whitelisted plugins.
# ---------------------------------------------------------------------------

module GraphicsGallery
  IMAGE_EXTS = %w[.gif .png .jpg .jpeg .webp .avif .svg .apng].freeze

  class Generator < Jekyll::Generator
    safe true
    priority :normal

    def generate(site)
      root = File.join(site.source, "graphics")
      return unless Dir.exist?(root)

      meta = site.data["graphics"] || {}
      folders = []

      Dir.children(root).sort.each do |entry|
        dir = File.join(root, entry)
        next unless File.directory?(dir)

        images = Dir.children(dir)
                    .select { |f| IMAGE_EXTS.include?(File.extname(f).downcase) }
                    .sort_by(&:downcase)
                    .map do |f|
                      {
                        "src"      => "/graphics/#{entry}/#{f}",
                        "filename" => f,
                        "name"     => File.basename(f, ".*").tr("_-", "  ")
                      }
                    end

        next if images.empty? # empty folder = not published

        info = meta[entry] || {}
        folder = {
          "slug"        => entry,
          "name"        => info["name"] || humanise(entry),
          "description" => info["description"],
          "url"         => "/graphics/#{entry}/",
          "count"       => images.size,
          "images"      => images,
          "cover"       => images.first["src"]
        }

        folders << folder
        site.pages << FolderPage.new(site, folder)
      end

      # /graphics/ reads this
      site.data["graphics_folders"] = folders
      Jekyll.logger.info "Graphics:", "#{folders.size} folders, " \
                                      "#{folders.sum { |f| f['count'] }} images"
    end

    private

    def humanise(slug)
      # "88x31" stays "88x31"; "pixel-art" becomes "Pixel art"
      return slug if slug =~ /\A[\dx]+\z/i
      slug.tr("_-", "  ").split.map(&:capitalize).join(" ")
    end
  end

  class FolderPage < Jekyll::Page
    def initialize(site, folder)
      @site = site
      @base = site.source
      @dir  = File.join("graphics", folder["slug"])
      @name = "index.html"

      process(@name)

      self.data = {
        "layout"    => "gallery",
        "title"     => folder["name"],
        "subtitle"  => folder["description"],
        "folder"    => folder,
        "permalink" => folder["url"]
      }
      self.content = ""
    end
  end
end
