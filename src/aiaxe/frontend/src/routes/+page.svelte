<script>
  let rand = "";

  async function getRand() {
    try {
      const response = await fetch("/aiaxe/rand");
      rand = await response.text();
    } catch (error) {
      console.error("Failed to fetch random number:", error);
      rand = "Error fetching number";
    }
  }
</script>

<h1>Welcome to your library project</h1>
<p>
  Create your package using @sveltejs/package and preview/showcase your work
  with SvelteKit
</p>
<p>
  Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the
  documentation
</p>
<h1>Your number is {rand ?? "Not fetched yet"}!</h1>
<button on:click={getRand}>Get a random number</button>
