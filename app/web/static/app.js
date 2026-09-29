:root {
  --bg: #030b14;
  --bg-2: #061924;
  --panel: rgba(5, 17, 27, 0.75);
  --panel-strong: rgba(7, 22, 34, 0.9);
  --primary: #2ad3ff;
  --primary-2: #8af8ff;
  --secondary: #0f4c68;
  --danger: #ff4d6d;
  --warning: #ffc857;
  --text: #dfefff;
  --muted: #7cc9d9;
  --border: rgba(42, 211, 255, 0.45);
  --shadow: rgba(42, 211, 255, 0.4);
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  min-height: 100vh;
  font-family: "Segoe UI", sans-serif;
  background:
    radial-gradient(circle at center, rgba(42, 211, 255, 0.08), transparent 25%),
    linear-gradient(135deg, #02070d 0%, #030d16 38%, #061728 100%);
  color: var(--text);
}

.hud-shell {
  width: min(1280px, 92vw);
  margin: 40px auto;
  padding: 18px;
  border: 1px solid var(--border);
  background: rgba(4, 10, 18, 0.78);
  box-shadow: 0 0 35px rgba(42, 211, 255, 0.1), inset 0 0 18px rgba(42, 211, 255, 0.08);
  border-radius: 18px;
}

.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 18px;
  border-bottom: 1px solid rgba(42, 211, 255, 0.12);
}

.brand-name {
  font-size: clamp(1.8rem, 2vw, 2.3rem);
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--primary-2);
}

.brand-subtitle {
  display: block;
  margin-top: 8px;
  font-size: 0.7rem;
  letter-spacing: 0.25em;
  color: var(--muted);
}

.badge {
  display: inline-block;
  padding: 8px 16px;
  border: 1px solid var(--border);
  border-radius: 999px;
  background: rgba(12, 23, 32, 0.8);
  color: var(--primary-2);
  letter-spacing: 0.12em;
  font-size: 0.7rem;
}

.badge.active {
  box-shadow: 0 0 18px rgba(42, 211, 255, 0.25);
}

.dashboard {
  display: grid;
  grid-template-columns: 1.5fr 0.85fr;
  gap: 18px;
  margin-top: 22px;
}

.core-panel,
.side-panel,
.lower-panel {
  background: var(--panel);
  border: 1px solid rgba(42, 211, 255, 0.18);
  border-radius: 18px;
  min-height: 200px;
  box-shadow: inset 0 0 32px rgba(10, 36, 47, 0.55);
}

.center-panel {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 24px 18px 18px;
}

.orbital-ring {
  position: relative;
  width: min(440px, 60vw);
  height: min(440px, 60vw);
  border-radius: 50%;
  border: 1px solid rgba(42, 211, 255, 0.5);
  box-shadow: inset 0 0 30px rgba(42, 211, 255, 0.12), 0 0 25px rgba(42, 211, 255, 0.08);
  display: grid;
  place-items: center;
  animation: rotate 15s linear infinite;
}

.orbital-ring::before,
.orbital-ring::after {
  content: "";
  position: absolute;
  inset: 15%;
  border-radius: 50%;
  border: 1px solid rgba(42, 211, 255, 0.24);
}

.core-orb {
  position: relative;
  width: 48%;
  height: 48%;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(138, 248, 255, 0.9), rgba(20, 120, 180, 0.45) 45%, rgba(5, 20, 30, 0.85) 68%);
  box-shadow: 0 0 40px rgba(42, 211, 255, 0.42);
}

.pulse-core {
  position: absolute;
  inset: 18%;
  border-radius: 50%;
  border: 1px solid rgba(138, 248, 255, 0.8);
  animation: pulse 2.8s ease-in-out infinite;
}

.metrics-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(120px, 1fr));
  width: 100%;
  gap: 14px;
  margin-top: 22px;
}

.metric-item {
  background: rgba(12, 25, 37, 0.72);
  border: 1px solid rgba(42, 211, 255, 0.12);
  border-radius: 12px;
  padding: 12px 10px;
  text-align: center;
}

.metric-item .label {
  display: block;
  font-size: 0.7rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
}

.metric-item .value {
  display: block;
  margin-top: 8px;
  font-size: 1.3rem;
  color: var(--primary-2);
}

.side-panel {
  padding: 16px;
}

.panel-block {
  margin-bottom: 20px;
}

.panel-block h3, .lower-panel h3 {
  margin: 0 0 12px;
  font-size: 0.8rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
}

.status-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 10px;
  color: var(--text);
}

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  padding: 8px 10px;
  border-radius: 999px;
  border: 1px solid rgba(42, 211, 255, 0.18);
  background: rgba(7, 23, 35, 0.7);
  color: var(--primary-2);
  font-size: 0.72rem;
}

.lower-panel {
  padding: 16px;
}

.history-list {
  display: grid;
  gap: 10px;
}

.history-item {
  padding: 10px 12px;
  border-radius: 10px;
  background: rgba(8, 22, 32, 0.7);
  border: 1px solid rgba(42, 211, 255, 0.1);
  color: var(--muted);
}

.action-row {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.control-button {
  border: 1px solid rgba(42, 211, 255, 0.3);
  background: linear-gradient(135deg, rgba(11, 28, 37, 0.94), rgba(14, 39, 50, 0.72));
  color: var(--text);
  padding: 12px 14px;
  border-radius: 10px;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.control-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 0 18px rgba(42, 211, 255, 0.18);
  border-color: rgba(42, 211, 255, 0.5);
}

.control-button.danger {
  border-color: rgba(255, 77, 109, 0.5);
  color: #ffd6dd;
}

@keyframes rotate {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@keyframes pulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.08); opacity: 0.7; }
}
