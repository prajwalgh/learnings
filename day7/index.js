// DOM Elements
const circles = document.querySelectorAll(".circle");
const progressBar = document.querySelector(".indicator");
const buttons = document.querySelectorAll("button");

let currentStep = 0; // Initialize currentStep to 0 for clarity

// Function to update steps and DOM
const updateSteps = (e) => {
  const increment = e.target.id === "next" ? 1 : -1; // Determine whether to increment or decrement
  currentStep += increment; // Update currentStep

  // Loop through circles to add/remove "active" class based on currentStep
  circles.forEach((circle, index) => {
    circle.classList.toggle("active", index < currentStep);
  });

  // Update progress bar width based on currentStep
  const progressWidth = (currentStep / (circles.length - 1)) * 100;
  progressBar.style.width = `${progressWidth}%`;

  // Disable/enable buttons based on currentStep
  buttons[0].disabled = currentStep === 0;
  buttons[1].disabled = currentStep === circles.length - 1;
};

buttons.forEach((button)=>{
   button.addEventListener("click",updateSteps);
   })
