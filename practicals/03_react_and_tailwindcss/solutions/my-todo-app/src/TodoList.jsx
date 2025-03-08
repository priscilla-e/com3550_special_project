import { useState } from "react";
import TaskItem from "./TaskItem";

function TodoList() {
  const [tasks, setTasks] = useState([
    { id: 1, text: "Learn React basics" },
    { id: 2, text: "Build a todo app" },
    { id: 3, text: "Style with Tailwind CSS" },
  ]);

  const [newTaskText, setNewTaskText] = useState("");

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

  // Function to delete a task
  const deleteTask = (taskId) => {
    const updatedTasks = tasks.filter((task) => task.id !== taskId);
    setTasks(updatedTasks);
  };

  return (
    <div>
      <div>
        <input
          type="text"
          value={newTaskText}
          onChange={(e) => setNewTaskText(e.target.value)}
          placeholder="Add a new task..."
        />
        <button onClick={addTask}>Add</button>
      </div>

      <ul>
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
