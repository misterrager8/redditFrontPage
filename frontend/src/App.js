import "./App.css";
import ContextProvider from "./context";
import Display from "./Display";

function App() {
  return (
    <ContextProvider>
      <Display />
    </ContextProvider>
  );
}

export default App;
