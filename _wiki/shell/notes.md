# notes.md

## TikTok JSON metadata output
The `-j` flag outputs JSON metadata.

Relevant fields mentioned in the source:
- `"track"` → Song title
- `"artist"` → Artist name, if official
- `"title"` → Often includes `Original sound` when the audio is user-created
- `"webpage_url"` → The source URL

## TikTok printed title behavior
The title-printing command can output one of these formats depending on the source:
- `Song Title - Artist` for an official song
- `original sound - username` for an original sound

## TikTok batch input note
If you have a text file named `links.txt`, it can contain TikTok audio URLs for batch processing.

## TikTok batch output example
Example output shown in the source:

```text
original sound - user123 | https://www.tiktok.com/music/7393372402044094480
Song Title - Artist | https://www.tiktok.com/music/7263468507952810798
```

## TikTok automation note
`yt-dlp` can automate this workflow by taking a list of links and printing the fields you want.

## Introductory note about finding shell scripts
Use these commands to find shell scripts on a Mac.

## Common locations you may find
The source says you will likely find items such as:
- `~/.zshrc`, `~/.zprofile` as config files
- `/usr/local/bin/brew` as the Homebrew launcher
- `/usr/local/bin/tesseract` as an OCR tool
- Various Homebrew tool scripts
- Possible `~/.local/bin/` scripts

## Interrupted full-system search note
A full-system `find / ...` search was stopped because it was producing too much output.

## Advice after stopping the full search
Full system searches can overwhelm you with system files, so narrower home-directory-focused searches are a better fit.

## What the personal-script scan gives you
The source describes these likely result categories:
- `~/.zshrc` and `~/.zprofile` as config files
- Any `~/scripts/` or `~/.local/bin/` personal scripts
- Homebrew tools such as `brew` and `tesseract`
- Less system noise overall

## Personal script count guidance
The source notes that many users have roughly 5 to 15 personal scripts total.

## Example executable output session
The source includes this captured terminal output:

```text
/Users/elianatamrat/bin/gpush
/Users/elianatamrat/bin/gpush_inc
/Users/elianatamrat/.local/bin/yt-dlp
/Users/elianatamrat/.nvm/nvm-exec
/Users/elianatamrat/.nvm/test/mocks/isainfo_x86
/Users/elianatamrat/.nvm/test/mocks/uname_smartos_x86
/Users/elianatamrat/.nvm/test/mocks/pkg_info_x86
/Users/elianatamrat/.nvm/test/mocks/uname_osx_amd64
/Users/elianatamrat/.nvm/test/mocks/uname_osx_x86
/Users/elianatamrat/.nvm/test/mocks/pkg_info_amd64
/Users/elianatamrat/.nvm/test/mocks/uname_linux_armv8l
/Users/elianatamrat/.nvm/test/mocks/isainfo_amd64
/Users/elianatamrat/.nvm/test/mocks/pkg_info_fail
/Users/elianatamrat/.nvm/test/mocks/uname_smartos_amd64
/Users/elianatamrat/.nvm/test/install_script/install_nvm_from_git
/Users/elianatamrat/.nvm/test/install_script/nvm_check_global_modules
/Users/elianatamrat/.nvm/test/install_script/nvm_download
/Users/elianatamrat/.nvm/test/install_script/nvm_reset
/Users/elianatamrat/.nvm/test/install_script/nvm_install_with_node_version
/Users/elianatamrat/.nvm/test/install_script/nvm_install_with_aliased_dot
```

## Interpreted personal scripts
The source interprets these as the actual useful personal scripts:
- `/Users/elianatamrat/bin/gpush` as a Git push script
- `/Users/elianatamrat/bin/gpush_inc` as a Git push-plus-increment script
- `/Users/elianatamrat/.local/bin/yt-dlp` as a YouTube downloader

## Interpreted NVM test files
The source marks these as ignorable NVM-related test files:
- `/Users/elianatamrat/.nvm/test/mocks/*`
- `/Users/elianatamrat/.nvm/*install_script*`

## Clean setup note
The source characterizes the setup this way:
- `~/bin/` for Git helpers
- `~/.local/bin/` for `yt-dlp`
- No clutter elsewhere

## Safety note about head -15
Using `head -15` limits output to 15 lines maximum.

## Why that command is considered safe
The explanation in the source breaks down the command this way:

```text
find ~          ← Only YOUR home directory (~10GB max)
-name "*.sh"    ← Only .sh files
| head -15      ← Stops after 15 lines
2>/dev/null     ← Hides permission errors
```

## Expected output guidance
The source says the command may show:
- `~/.zshrc` and `~/.zprofile`
- Possibly some NVM scripts
- `~/bin/` Git helpers if they end in `.sh`

## Stop behavior note
Ctrl+C can be used to stop the command early.
