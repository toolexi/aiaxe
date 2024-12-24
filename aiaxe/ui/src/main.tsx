import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
// import "./index.css";
import Home from "./components/Home";
import Navbar from "./components/Navbar";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <Navbar />
    <Home />
  </StrictMode>
);
