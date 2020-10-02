import React from "react";
import "./Header.css";
import { Link } from "react-router-dom";

function Header() {
  return (
    <div className="navbar">
      <Link to="/" style={{ textDecoration: "none", color: "white" }}>
        <div className="title">
          <h1>MUSE</h1>
        </div>
      </Link>
      <div className="buttons">
        <Link
          to="/list"
          style={{
            textDecoration: "none",
            color: "white",
            marginRight: "2vw",
          }}
        >
          <h3>All Images</h3>
        </Link>
      </div>
    </div>
  );
}

export default Header;
