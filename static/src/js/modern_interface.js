// Modern Change Request Interface JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Add modern styling to form fields
    const formFields = document.querySelectorAll('input, select, textarea');
    formFields.forEach(field => {
        field.classList.add('form-control');
        
        // Add focus effects
        field.addEventListener('focus', function() {
            this.style.borderColor = '#667eea';
            this.style.boxShadow = '0 0 0 3px rgba(102, 126, 234, 0.1)';
        });
        
        field.addEventListener('blur', function() {
            this.style.borderColor = '#e1e5e9';
            this.style.boxShadow = 'none';
        });
    });
    
    // Add modern styling to buttons
    const buttons = document.querySelectorAll('button');
    buttons.forEach(button => {
        if (button.textContent.includes('Submit')) {
            button.classList.add('btn-modern', 'btn-primary-modern');
        } else if (button.textContent.includes('Approve')) {
            button.classList.add('btn-modern', 'btn-success-modern');
        } else if (button.textContent.includes('Reject')) {
            button.classList.add('btn-modern', 'btn-warning-modern');
        } else if (button.textContent.includes('Complete')) {
            button.classList.add('btn-modern', 'btn-info-modern');
        } else if (button.textContent.includes('Export')) {
            button.classList.add('btn-modern', 'btn-primary-modern');
        }
    });
    
    // Add hover effects to cards
    const cards = document.querySelectorAll('.change-request-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 20px 40px rgba(0, 0, 0, 0.15)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.1)';
        });
    });
    
    // Add progress bar functionality
    const progressBar = document.querySelector('.progress-fill');
    if (progressBar) {
        let progress = 0;
        const interval = setInterval(() => {
            progress += Math.random() * 10;
            if (progress > 45) progress = 45;
            progressBar.style.width = progress + '%';
            if (progress >= 45) clearInterval(interval);
        }, 500);
    }
    
    // Add notification system
    function showNotification(message, type = 'success') {
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 15px 20px;
            border-radius: 8px;
            color: white;
            font-weight: 500;
            z-index: 1000;
            animation: slideInRight 0.3s ease;
            background: ${type === 'success' ? 'linear-gradient(135deg, #56ab2f 0%, #a8e6cf 100%)' : 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)'};
        `;
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.remove();
        }, 3000);
    }
    
    // Add button click animations
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (this.classList.contains('btn-modern')) {
                // Add loading effect
                const originalText = this.innerHTML;
                this.innerHTML += '<span style="margin-left: 8px; display: inline-block; width: 16px; height: 16px; border: 2px solid #ffffff; border-top: 2px solid transparent; border-radius: 50%; animation: spin 1s linear infinite;"></span>';
                this.disabled = true;
                
                setTimeout(() => {
                    this.innerHTML = originalText;
                    this.disabled = false;
                    showNotification('Action completed successfully!');
                }, 1500);
            }
        });
    });
    
    // Add CSS animations
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideInRight {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .fade-in {
            animation: fadeIn 0.5s ease-in;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    `;
    document.head.appendChild(style);
    
    // Add fade-in animation to form sections
    const formSections = document.querySelectorAll('.form-section');
    formSections.forEach((section, index) => {
        setTimeout(() => {
            section.classList.add('fade-in');
        }, index * 100);
    });
});
