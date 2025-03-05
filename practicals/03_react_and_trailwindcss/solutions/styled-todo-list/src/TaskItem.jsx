import './TaskItem.css';

function TaskItem({ id, text, onDelete }) {
  return (
    <li className="task-item">
      <span>{text}</span>
      <button onClick={onDelete}>Delete</button>
    </li>
  );
}

export default TaskItem;
