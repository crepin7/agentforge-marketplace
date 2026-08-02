import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        forge: { 50: "#fff7ed", 500: "#f97316", 600: "#ea580c", 900: "#7c2d12" },
      },
    },
  },
  plugins: [],
};
export default config;
