import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import Home from "./components/Home";
import { NavbarTop } from "./components/Navbar";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <div className="container">
      <NavbarTop />
      <Home />
    </div>
  </StrictMode>
);
