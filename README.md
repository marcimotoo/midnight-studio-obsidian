# Midnight Studio

A quiet dark theme for Obsidian, with charcoal surfaces, readable text, and bright **#00FF99** mint accents.

## Design

- Subtle accents for active tabs, selected files, links, and checkboxes.
- Soft secondary colors for code blocks and status indicators.
- Styled headings, tables, tags, quotes, and callouts.
- No external fonts, remote assets, or community plugins required.
- Your font choices and font size remain configurable in Obsidian.

**Supported mode: Dark.** Light mode uses Obsidian's default appearance.

## Manual installation

1. Download `theme.css` and `manifest.json` from the latest GitHub release.
2. Create a folder named `Midnight Studio` inside your vault's `.obsidian/themes` folder.
3. Place both files directly inside that folder. Ensure the filenames are exactly `theme.css` and `manifest.json`.
4. In Obsidian, open **Settings → Appearance**, select **Dark** as the base color scheme, and choose **Midnight Studio** from the theme list.

Community-directory installation becomes available after the theme is submitted and approved.

## Development

Edit `theme.css` to adjust the theme. Install the development dependencies with `npm ci`, then run `npm run lint` to check the CSS using Obsidian's theme-review rules.

To release an update, increment the version in `manifest.json` and `package.json`, add its minimum supported Obsidian version to `versions.json`, and push a matching Git tag without a `v` prefix. The release workflow creates a draft GitHub release with the two required theme files attached. Review and publish the draft before submitting or updating the theme in the directory.

## Feedback

Report issues or suggest improvements in [GitHub Issues](https://github.com/marcimotoo/midnight-theme-obsidian/issues). Include your Obsidian version and a screenshot where useful. Remove private note content before sharing screenshots.

## License

MIT. You may use, modify, and share the theme under the terms in [LICENSE](LICENSE).
