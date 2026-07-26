// Helper to parse comma-separated string input into a cleaned array of tags
function parseTagsInput(inputValue) {
  if (!inputValue) return [];
  return inputValue
    .split(',')
    .map(tag => tag.trim())
    .filter(tag => tag.length > 0);
}

function createCard(task) {
  const card = document.createElement('div');
  card.className = 'task-card';

  // Format due date rendering
  const dueDateHtml = task.due_date ? `<span class="due-date">Due: ${task.due_date}</span>` : '';
  
  // Render overdue badge if true
  const overdueBadgeHtml = task.is_overdue 
    ? `<span class="pill overdue" style="background-color: #ff4d4f; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.8rem;">Overdue</span>` 
    : '';

  // Render tag pills array
  const tagsHtml = (task.tags && task.tags.length > 0)
    ? `<div class="tags-container" style="margin-top: 8px; display: flex; gap: 4px; flex-wrap: wrap;">
        ${task.tags.map(tag => `<span class="pill tag" style="background-color: #e6f7ff; color: #1890ff; padding: 2px 8px; border-radius: 12px; font-size: 0.75rem;">#${tag}</span>`).join('')}
       </div>`
    : '';

  card.innerHTML = `
    <h3>${task.title} ${overdueBadgeHtml}</h3>
    <p>${task.description || ''}</p>
    ${dueDateHtml}
    ${tagsHtml}
  `;

  return card;
}

// Fetch tasks with both overdue_only AND tag filters
async function loadTasks() {
  const isOverdueOnly = document.getElementById('overdue_filter').checked;
  const tagFilter = document.getElementById('tag_filter') ? document.getElementById('tag_filter').value.trim() : '';

  // Build dynamic URL search query parameters
  const params = new URLSearchParams();
  if (isOverdueOnly) params.append('overdue_only', 'true');
  if (tagFilter) params.append('tag', tagFilter);

  const response = await fetch(`/tasks?${params.toString()}`);
  const tasks = await response.json();
  
  const container = document.getElementById('task_list'); // adjust ID if needed
  if (container) {
    container.innerHTML = '';
    tasks.forEach(task => container.appendChild(createCard(task)));
  }
}

// Function to attach when submitting the create task modal form
async function handleCreateTask(event) {
  event.preventDefault();

  const title = document.getElementById('title').value;
  const description = document.getElementById('description').value;
  const dueDate = document.getElementById('due_date').value;
  const tagsRaw = document.getElementById('tags') ? document.getElementById('tags').value : '';

  const payload = {
    title: title,
    description: description,
    due_date: dueDate || null,
    tags: parseTagsInput(tagsRaw) // Converts "dev, urgent" -> ["dev", "urgent"]
  };

  const response = await fetch('/tasks', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });

  if (response.ok) {
    loadTasks(); // Reload task list on success
  } else {
    const errorData = await response.json();
    alert(`Error: ${errorData.detail?.[0]?.msg || 'Validation failed'}`);
  }
}

// Event Listeners
document.getElementById('overdue_filter').addEventListener('change', loadTasks);

const tagFilterInput = document.getElementById('tag_filter');
if (tagFilterInput) {
  tagFilterInput.addEventListener('input', loadTasks);
}