import React from "react";
import "./App.css";
import Header from "./components/Header.js";
// import Gallery from "./components/Gallery.js";
// import List from "./components/List.js";
import axios from "axios";
import { Route, HashRouter } from "react-router-dom";

function App() {
  return (
    <HashRouter basename="/">
      <div className="app">
        <Header />
        {/* <main>
          <Route
            exact
            path="/"
            render={({ match }) => <Gallery match={match} />}
          />
          <Route
            exact
            path="/gallery"
            render={({ match }) => <Gallery match={match} />}
          />
          <Route
            exact
            path="/list"
            render={({ match }) => <List match={match} />}
          />
        </main> */}
      </div>
    </HashRouter>
  );
}

export default App;
