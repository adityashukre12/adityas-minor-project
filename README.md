const display = document.getElementById('display');
const buttons = document.querySelectorAll('.btn');

let currentExpression = '0';
let justEvaluated = false;

function updateDisplay(value) {
  display.textContent = value;
}

function appendValue(value) {
  if (justEvaluated && /[0-9.]/.test(value)) {
    currentExpression = '';
    justEvaluated = false;
  }

  if (currentExpression === '0' && /[0-9]/.test(value)) {
    currentExpression = value;
  } else {
    currentExpression += value;
  }

  updateDisplay(currentExpression);
}

function handleOperator(operator) {
  if (justEvaluated) {
    justEvaluated = false;
  }

  const lastChar = currentExpression.slice(-1);
  if (['+', '-', '*', '/', '%'].includes(lastChar)) {
    currentExpression = currentExpression.slice(0, -1) + operator;
  } else {
    currentExpression += operator;
  }

  updateDisplay(currentExpression);
}

function handleDecimal() {
  if (justEvaluated) {
    currentExpression = '0';
    justEvaluated = false;
  }

  const parts = currentExpression.split(/[+\-*/%]/);
  const lastPart = parts[parts.length - 1];

  if (!lastPart.includes('.')) {
    currentExpression += '.';
  }

  updateDisplay(currentExpression);
}

function clearDisplay() {
  currentExpression = '0';
  justEvaluated = false;
  updateDisplay(currentExpression);
}

function deleteLast() {
  if (justEvaluated) {
    clearDisplay();
    return;
  }

  currentExpression = currentExpression.slice(0, -1) || '0';
  updateDisplay(currentExpression);
}

function calculateExpression() {
  try {
    const sanitized = currentExpression
      .replace(/×/g, '*')
      .replace(/÷/g, '/');

    if (!sanitized || sanitized === '.') {
      return;
    }

    const result = Function(`"use strict"; return (${sanitized});`)();

    if (!Number.isFinite(result)) {
      throw new Error('Invalid expression');
    }

    currentExpression = Number.isInteger(result) ? String(result) : String(parseFloat(result.toFixed(10)));
    justEvaluated = true;
    updateDisplay(currentExpression);
  } catch (error) {
    currentExpression = 'Error';
    justEvaluated = true;
    updateDisplay(currentExpression);
  }
}

buttons.forEach((button) => {
  button.addEventListener('click', () => {
    const value = button.dataset.value;
    const action = button.dataset.action;

    if (action === 'clear') {
      clearDisplay();
      return;
    }

    if (action === 'delete') {
      deleteLast();
      return;
    }

    if (action === 'equals') {
      calculateExpression();
      return;
    }

    if (value === '.') {
      handleDecimal();
      return;
    }

    if (['+', '-', '*', '/', '%'].includes(value)) {
      handleOperator(value);
      return;
    }

    if (currentExpression === 'Error') {
      currentExpression = '0';
    }

    appendValue(value);
  });
});

updateDisplay(currentExpression);
