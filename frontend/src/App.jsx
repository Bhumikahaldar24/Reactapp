
import "./App.css";
import { SearchBar } from "./components/SearchBar";


function App() {

  return (
    <div className="App">
      <div className="search-bar-container">
        <SearchBar/>
        <div>SeacrhResults</div>
      </div>
    </div>
  );
}

export default App;