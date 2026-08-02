import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "AgentForge — AI Agent Marketplace",
  description: "Decouvrez, deployez et monetisez des agents IA specialises.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="fr">
      <body className="bg-slate-950 text-slate-100 antialiased">{children}</body>
    </html>
  );
}
