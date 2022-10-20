var themeFlag = 0; //0 for light and 1 for dark theme
function toggleDark() {
    var element = document.body;
    element.classList.toggle("dark-mode");
}
function toggleTheme(x) {
    if (themeFlag == 0) {
        x.innerHTML = `<span class="material-symbols-outlined light-icon">
                    wb_sunny
                </span>`;
        themeFlag = 1;
    }
    else {
        x.innerHTML = `<span class="material-symbols-outlined dark-icon">
                    dark_mode
                </span>`;
        themeFlag = 0;
    }

}
