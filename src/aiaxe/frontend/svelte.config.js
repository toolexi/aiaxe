import adapter from '@sveltejs/adapter-auto';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: vitePreprocess(),

	kit: {
		adapter: adapter({
			pages: "frontend/public",
			assets: "frontend/public",
			fallback: null,
			precompress: false,
			strict: true,
		  })
	}
};

export default config;
