function toggleHighlightCheckbox() {
            const select = document.getElementById('task-select');
            const highlightGroup = document.getElementById('highlight-entities-group');
            highlightGroup.style.display = (select.value === 'summarization') ? 'flex' : 'none';
        }

        window.onload = toggleHighlightCheckbox;