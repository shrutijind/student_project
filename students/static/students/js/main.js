/* jshint esversion: 6, browser: true */

document.addEventListener('DOMContentLoaded', function () {
    const startDateInput = document.getElementById('id_start_date');
    const endDateInput = document.getElementById('id_end_date');
    const durationDisplay = document.getElementById('leave-duration-display');

    function calculateDays() {
        if (startDateInput && endDateInput && durationDisplay) {
            const startVal = startDateInput.value;
            const endVal = endDateInput.value;

            if (startVal && endVal) {
                const start = new Date(startVal);
                const end = new Date(endVal);

                if (end >= start) {
                    const diffTime = Math.abs(end - start);
                    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)) + 1;
                    durationDisplay.textContent = `Total Duration: ${diffDays} day(s)`;
                    durationDisplay.classList.remove('d-none');
                } else {
                    durationDisplay.textContent = 'End date cannot be earlier than start date.';
                    durationDisplay.classList.remove('d-none');
                }
            } else {
                durationDisplay.classList.add('d-none');
            }
        }
    }

    if (startDateInput && endDateInput) {
        // Restrict minimum selectable date to today
        const today = new Date().toISOString().split('T')[0];
        startDateInput.setAttribute('min', today);
        endDateInput.setAttribute('min', today);

        // Update end date min dynamically
        startDateInput.addEventListener('change', function () {
            if (this.value) {
                endDateInput.setAttribute('min', this.value);
            }
            calculateDays();
        });

        endDateInput.addEventListener('change', calculateDays);

        // Run calculation immediately on load if fields are pre-filled
        calculateDays();
    }

    // Auto-dismiss alert messages after 4 seconds
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 4000);
    });
});