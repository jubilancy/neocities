source "https://rubygems.org"

gem "jekyll", "~> 4.3"
gem "webrick"   # jekyll serve needs this on Ruby 3+

group :jekyll_plugins do
  # (none required — the graphics gallery uses a local _plugins/ generator,
  #  which works because we build with GitHub Actions, not GitHub Pages)
end

# Ruby 3.4 dropped these from the stdlib
gem "csv"
gem "base64"
gem "bigdecimal"
gem "logger"
