// const body = document.querySelector('body');
// const parallaxAmount = 5; // Adjust this value to control the intensity of the parallax effect
// const zoomFactor = 0.2; // Adjust this value to control the intensity of the zoom effect

// function updateBackground(event) {
//     const mouseX = event.clientX;
//     const mouseY = event.clientY;
//     const offsetX = mouseX / window.innerWidth - 0.5;
//     const offsetY = mouseY / window.innerHeight - 0.5;

//     const translateX = offsetX * parallaxAmount;
//     const translateY = offsetY * parallaxAmount;

//     const scale = 1 + (window.innerWidth / window.innerHeight - 1) * zoomFactor;

//     body.style.backgroundSize = `${125 * scale}% auto`;

//     const maxTranslateX = (scale - 1) * window.innerWidth / 2;
//     const maxTranslateY = (scale - 1) * window.innerHeight / 2;

//     const boundedTranslateX = Math.max(-maxTranslateX, Math.min(maxTranslateX, translateX));
//     const boundedTranslateY = Math.max(-maxTranslateY, Math.min(maxTranslateY, translateY));

//     body.style.backgroundPositionX = `calc(50% + ${boundedTranslateX}px)`;
//     body.style.backgroundPositionY = `calc(50% + ${boundedTranslateY}px)`;
// }

// function handleResize() {
//     updateBackground({ clientX: window.innerWidth / 2, clientY: window.innerHeight / 2 });
// }

// window.addEventListener('resize', handleResize);
// window.addEventListener('mousemove', updateBackground);
// handleResize(); // Initialize background on page load
