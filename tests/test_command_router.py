async function fetchStatus() {
  try {
    const headers = { 'X-API-Key': 'change-me' };
    const res = await fetch('/api/status', { headers });
    if (!res.ok) return;
    const data = await res.json();
    document.getElementById('status-value').textContent = data.status || 'ACTIVE';
    document.getElementById('night-mode').textContent = data.night_mode ? 'SI' : 'NO';
    document.getElementById('mic-value').textContent = data.microphone || 'ACTIVO';

    const stateBadge = document.getElementById('state-badge');
    stateBadge.textContent = data.status || 'ACTIVE';
    stateBadge.className = 'badge active';

    const plugins = data.plugins || [];
    const pluginList = document.getElementById('plugins-list');
    pluginList.innerHTML = plugins.map(p => `<span class="tag">${p.name}</span>`).join('');
  } catch (error) {
    console.error('Status fetch failed', error);
  }
}

async function fetchSystem() {
  try {
    const headers = { 'X-API-Key': 'change-me' };
    const res = await fetch('/api/system', { headers });
    if (!res.ok) return;
    const data = await res.json();
    document.getElementById('cpu-value').textContent = `${data.cpu_percent ?? 0}%`;
    document.getElementById('ram-value').textContent = `${data.memory_percent ?? 0}%`;
    document.getElementById('disk-value').textContent = `${data.disk_percent ?? 0}%`;
  } catch (error) {
    console.error('System fetch failed', error);
  }
}

async function fetchHistory() {
  try {
    const headers = { 'X-API-Key': 'change-me' };
    const res = await fetch('/api/memory', { headers });
    if (!res.ok) return;
    const data = await res.json();
    const list = document.getElementById('history-list');
    const items = data.items || {};
    const entries = Object.entries(items).slice(-6);
    list.innerHTML = entries.map(([key, value]) => `<div class="history-item">${key}: ${JSON.stringify(value)}</div>`).join('');
  } catch (error) {
    console.error('History fetch failed', error);
  }
}

async function stopAllActions() {
  const headers = { 'X-API-Key': 'change-me', 'Content-Type': 'application/json' };
  await fetch('/api/stop-all-actions', { method: 'POST', headers });
  fetchStatus();
}

[...document.querySelectorAll('.control-button')].forEach(button => {
  button.addEventListener('click', async () => {
    const action = button.dataset.action;
    const target = button.dataset.target;
    const headers = { 'X-API-Key': 'change-me', 'Content-Type': 'application/json' };
    await fetch('/api/command', {
      method: 'POST',
      headers,
      body: JSON.stringify({ action, target, confirmed: true })
    });
    fetchStatus();
  });
});

document.getElementById('stop-all').addEventListener('click', stopAllActions);

setInterval(async () => {
  await fetchStatus();
  await fetchSystem();
  await fetchHistory();
}, 4000);

fetchStatus();
fetchSystem();
fetchHistory();
