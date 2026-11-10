* {
  box-sizing: border-box;
}

body {
  margin: 0;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: linear-gradient(135deg, #0f172a, #1e293b);
  font-family: Arial, Helvetica, sans-serif;
}

.calculator {
  width: min(92vw, 360px);
  background: #111827;
  border-radius: 22px;
  padding: 20px;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.35);
}

.display {
  width: 100%;
  min-height: 85px;
  margin-bottom: 18px;
  padding: 16px 12px;
  border-radius: 12px;
  background: #0b1120;
  border: 1px solid rgba(255, 255, 255, 0.08);
  color: #f8fafc;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  font-size: clamp(2rem, 5vw, 2.8rem);
  overflow: hidden;
  word-break: break-all;
}

.buttons {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 12px;
}

.btn {
  border: none;
  border-radius: 14px;
  background: #1f2937;
  color: #f9fafb;
  font-size: 1.5rem;
  font-weight: 600;
  padding: 20px 10px;
  cursor: pointer;
  transition: transform 0.12s ease, filter 0.12s ease;
}

.btn:hover {
  filter: brightness(1.12);
}

.btn:active {
  transform: scale(0.98);
}

.btn.gray {
  background: #374151;
}

.btn.orange {
  background: #f59e0b;
  color: #111827;
}

.btn.zero {
  grid-column: span 2;
}
