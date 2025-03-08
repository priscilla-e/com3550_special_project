import { useState, useEffect } from "react";
import TaskItem from "./TaskItem";
import './TodoList.css';

function TodoList() {
  // Load tasks from localStorage on initial render
  const [tasks, setTasks] = useState(() => {
    const savedTasks = localStorage.getItem('tasks');
    if (savedTasks) {
      return JSON.parse(savedTasks);
    } else {
      return [
        { id: 1, text: "Learn React basics" },
        { id: 2, text: "Build a todo app" },
        { id: 3, text: "Style with Vanilla CSS" },
      ];
    }
  });

  const [newTaskText, setNewTaskText] = useState("");

  // Save tasks to localStorage whenever tasks change
  useEffect(() => {
    localStorage.setItem('tasks', JSON.stringify(tasks));
  }, [tasks]);

  // Function to add a new task
  const addTask = () => {
    if (newTaskText.trim() === "") return;

    const newTask = {
      id: Date.now(),
      text: newTaskText,
    };

    setTasks([...tasks, newTask]);
    setNewTaskText("");
  };

  // Function to handle Enter key press
  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      addTask();
    }
  };

  // Function to delete a task
  const deleteTask = (taskId) => {
    const updatedTasks = tasks.filter((task) => task.id !== taskId);
    setTasks(updatedTasks);
  };

  return (
    <div className="todo-container">
      <div className="add-task-form">
        <input
          type="text"
          value={newTaskText}
          onChange={(e) => setNewTaskText(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Add a new task..."
        />
        <button onClick={addTask}>Add Task</button>
      </div>

      <ul className="task-list">
        {tasks.map((task) => (
          <TaskItem
            key={task.id}
            id={task.id}
            text={task.text}
            onDelete={() => deleteTask(task.id)}
          />
        ))}
      </ul>
    </div>
  );
}

export default TodoList;
