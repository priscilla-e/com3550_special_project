import Header from "./Header";
import TodoList from "./TodoList";
import "./App.css";

function App() {
  return (
    <div className="app-container">
      <Header />
      <main className="card">
        <TodoList />
      </main>
    </div>
  );
}

export default App;
