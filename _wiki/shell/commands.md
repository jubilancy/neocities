---
---

# commands.md

## Fetch TikTok audio metadata as JSON
Gets full metadata for a TikTok audio page in JSON format.

```sh
yt-dlp -j "https://www.tiktok.com/music/7393372402044094480"
```

## Print the track, artist, or title for one TikTok audio URL
Outputs the best available audio name fields for a single TikTok sound link.

```sh
yt-dlp --print "%(track,artist,title)s" "https://www.tiktok.com/music/7393372402044094480"
```

## Print title and URL for a batch of TikTok audio links
Reads TikTok audio URLs from a text file and prints each title with its source URL.

```sh
yt-dlp --print "%(title)s | %(webpage_url)s" -a links.txt
```

## Find all executable shell scripts on the system
Searches the filesystem for executable shell script files with common shell extensions.

```bash
find / -type f \( -name "*.sh" -o -name "*.bash" -o -name "*.zsh" -o -name "*.fish" \) -perm +111 2>/dev/null
```

## List Homebrew shell scripts
Lists likely shell-script files in common Homebrew binary and scripts locations.

```bash
ls -la /usr/local/bin/*sh /usr/local/share/*/scripts/ 2>/dev/null
```

## List shell scripts in the home directory with details
Finds shell script files in the home directory and shows file metadata.

```bash
find ~ -type f \( -name "*.sh" -o -name "*.bash" -o -name "*.zsh" \) -exec ls -la {} + 2>/dev/null
```

## List common system shell scripts
Shows shell-related files in standard system binary and configuration locations.

```bash
ls -la /etc/*sh /usr/bin/*sh /usr/local/bin/*sh 2>/dev/null
```

## Find executable files with shell-like names
Searches common local paths for executable files whose names contain `sh` and limits output.

```bash
find /usr/local /opt/homebrew ~ -type f -perm +111 -name "*sh*" 2>/dev/null | head -20
```

## List shell-related dotfiles and config locations
Shows common shell config files and the main config directory.

```bash
ls -la ~/.z* ~/.bash* ~/.profile ~/.config/
```

## List the local bin directory or print a fallback message
Shows contents of `~/.local/bin` when present, otherwise prints a fallback note.

```bash
ls -la ~/.local/bin/ 2>/dev/null || echo "No ~/.local/bin"
```

## Filter shell script results to exclude vendor directories
Finds shell scripts in the home directory and excludes vendor and node_modules paths.

```bash
find ~ -name "*.sh" | grep -v "vendor\|node_modules"
```

## Find shell scripts in the home directory only
Searches only the home directory for common shell script file extensions.

```bash
find ~ -type f \( -name "*.sh" -o -name "*.bash" -o -name "*.zsh" \) 2>/dev/null
```

## Find executable files in the home directory
Lists executable files in the home directory tree and limits the output.

```bash
find ~ -type f -perm +111 2>/dev/null | head -20
```

## Quick scan of likely personal script locations
Lists likely personal script locations in the home directory and config areas.

```bash
ls -la ~/*sh ~/.local/bin/ ~/.config/ 2>/dev/null
```

## Find Homebrew shell scripts with grep
Lists Homebrew binaries and filters for files ending in `.sh` or `.zsh`.

```bash
ls -la /usr/local/bin/ | grep -E '\.sh$|\.zsh$'
```

## Find shell scripts in common shared directories
Searches common shared directories and the home directory for `.sh` files and limits output.

```bash
find /usr/local/share /opt ~ -name "*.sh" -type f 2>/dev/null | head -15
```

## Combine personal scripts and executable results
Shows a mixed list of home-directory scripts and executables, limited to 30 results.

```bash
( find ~ -type f \( -name "*.sh" -o -perm +111 \) ; find /usr/local/bin ~ -name "*.sh" ) 2>/dev/null | head -30
```

## View the gpush helper script
Prints the contents of the `gpush` script.

```bash
cat ~/bin/gpush
```

## View the gpush_inc helper script
Prints the contents of the `gpush_inc` script.

```bash
cat ~/bin/gpush_inc
```

## Inspect the yt-dlp executable file type
Shows what kind of file `yt-dlp` is.

```bash
file ~/.local/bin/yt-dlp
```

## Find shell scripts by extension and limit output
Searches the home directory for `.sh`, `.zsh`, and `.bash` files and limits output.

```bash
find ~ -name "*.sh" -o -name "*.zsh" -o -name "*.bash" 2>/dev/null | head -15
```

## Run the gpush helper
Executes the `gpush` helper command.

```bash
gpush
```

## Run the gpush_inc helper
Executes the `gpush_inc` helper command.

```bash
gpush_inc
```

## Check the yt-dlp version
Prints the installed `yt-dlp` version.

```bash
yt-dlp --version
```
