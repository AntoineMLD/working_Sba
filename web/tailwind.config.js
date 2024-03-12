/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}",
            "./main/templates/**/*.{html,js}",
],
theme: {
  extend: {
    // Définition des couleurs personnalisées
    colors: {
      'navbar-bg': 'hsl(210, 50%, 15%)',
      'navbar-text': 'hsl(210, 20%, 80%)',
      'navbar-text-focus': 'hsl(203, 100%, 50%)',
      'navbar-bg-contrast': 'hsl(210, 50%, 25%)',
    },
    // Autres ajustements de thème si nécessaire
    spacing: {
      '100': '25rem', // Exemple d'ajout d'une nouvelle valeur de spacing
    },
    borderRadius: {
      'large': '12px',
    },
    fontFamily: {
      'sans': ['Arial', 'Helvetica', 'sans-serif'],
    },
    boxShadow: {
      'navbar': '0 2px 4px rgba(0, 0, 0, 0.15)',
      'menu': '0 0 20px rgba(0, 0, 0, 0.3)',
    },
  },
},
plugins: [],
};