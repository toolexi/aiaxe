import cssInjectedByJsPlugin from "vite-plugin-css-injected-by-js";

import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vite.dev/config/
export default defineConfig({
  base: "./",
  plugins: [
    react(),
    {
      name: "transform-url-src",
      transformIndexHtml: (html) =>
        html
          .replace(`src="/assets/`, `src="/static/assets/`)
          .replace(`href="/`, `href="/ui/`),
    },
    cssInjectedByJsPlugin(),
  ],
  build: {
    assetsDir: "static/assets",
  },
});
