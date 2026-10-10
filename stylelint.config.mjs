import obsidianConfig from "stylelint-config-obsidianmd";

export default {
  ...obsidianConfig,
  rules: {
    ...obsidianConfig.rules,
    "color-hex-length": "long"
  }
};
