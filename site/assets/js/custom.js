document$.subscribe(function() {
  // Initialize Termynal instances
  document.querySelectorAll('.termynal').forEach(node => {
    new Termynal(node, {
      lineDelay: 500,
      noInit: true
    });
  });
  
  // Add copy buttons to code blocks
  document.querySelectorAll('pre code').forEach(code => {
    const button = document.createElement('button');
    button.className = 'md-clipboard';
    button.innerHTML = '<span class="twemoji"><svg>...</svg></span>';
    code.parentNode.insertBefore(button, code);
  });
});