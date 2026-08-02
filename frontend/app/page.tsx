import Link from "next/link";

const FEATURED = [
  { slug: "trader-sage", name: "Trader Sage", tagline: "Signaux de trading IA multi-actifs", price: "49$/mois", tag: "Finance" },
  { slug: "code-wizard", name: "Code Wizard", tagline: "Code review, refactor, tests", price: "29$/mois", tag: "Dev" },
  { slug: "growth-hacker", name: "Growth Hacker", tagline: "Strategies d acquisition + copywriting", price: "39$/mois", tag: "Marketing" },
  { slug: "data-analyst", name: "Data Analyst", tagline: "SQL auto, dashboards, insights", price: "39$/mois", tag: "Data" },
  { slug: "support-hero", name: "Support Hero", tagline: "Support client multilingue 24/7", price: "19$/mois", tag: "Support" },
  { slug: "legal-eagle", name: "Legal Eagle", tagline: "Contrats, conformite RGPD", price: "59$/mois", tag: "Legal" },
];

export default function HomePage() {
  return (
    <main className="min-h-screen">
      <section className="relative overflow-hidden border-b border-slate-800">
        <div className="mx-auto max-w-6xl px-6 py-24 text-center">
          <p className="mb-4 inline-block rounded-full border border-forge-500/40 bg-forge-500/10 px-3 py-1 text-xs uppercase tracking-wider text-forge-500">
            MVP v0.1 · En acces anticipe
          </p>
          <h1 className="bg-gradient-to-br from-white to-slate-400 bg-clip-text text-5xl font-extrabold tracking-tight text-transparent md:text-7xl">
            La forge a agents IA
          </h1>
          <p className="mx-auto mt-6 max-w-2xl text-lg text-slate-300">
            Decouvrez, deployez et monetisez des agents IA specialises — trading, code, marketing, data, support, legal. Un seul abonnement, mille competences.
          </p>
          <div className="mt-10 flex flex-wrap justify-center gap-4">
            <Link href="#agents" className="rounded-lg bg-forge-500 px-6 py-3 font-semibold text-white transition hover:bg-forge-600">
              Explorer les agents →
            </Link>
            <Link href="https://github.com/crepin7/agentforge-marketplace" className="rounded-lg border border-slate-700 px-6 py-3 font-semibold text-slate-200 transition hover:border-slate-500">
              GitHub ↗
            </Link>
          </div>
        </div>
      </section>

      <section id="agents" className="mx-auto max-w-6xl px-6 py-20">
        <h2 className="mb-2 text-3xl font-bold">Agents vedettes</h2>
        <p className="mb-10 text-slate-400">6 agents prets a l'emploi, plus ajoutes chaque semaine.</p>
        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {FEATURED.map((a) => (
            <Link key={a.slug} href={`/agents/${a.slug}`} className="group rounded-xl border border-slate-800 bg-slate-900/50 p-6 transition hover:border-forge-500/60 hover:bg-slate-900">
              <div className="mb-3 flex items-center justify-between">
                <span className="rounded-md bg-slate-800 px-2 py-0.5 text-xs text-slate-300">{a.tag}</span>
                <span className="text-sm font-semibold text-forge-500">{a.price}</span>
              </div>
              <h3 className="mb-2 text-xl font-semibold group-hover:text-forge-500">{a.name}</h3>
              <p className="text-sm text-slate-400">{a.tagline}</p>
            </Link>
          ))}
        </div>
      </section>

      <section className="border-t border-slate-800 bg-gradient-to-b from-slate-950 to-slate-900">
        <div className="mx-auto max-w-4xl px-6 py-20 text-center">
          <h2 className="text-3xl font-bold">Pret a forger votre avantage IA ?</h2>
          <p className="mt-4 text-slate-400">All Access : 99$/mois — acces illimite a tous les agents. Annulable a tout moment.</p>
          <Link href="#" className="mt-8 inline-block rounded-lg bg-forge-500 px-8 py-3 font-semibold text-white transition hover:bg-forge-600">
            Demarrer maintenant
          </Link>
        </div>
      </section>

      <footer className="border-t border-slate-800 py-8 text-center text-sm text-slate-500">
        © 2026 AgentForge · MIT License
      </footer>
    </main>
  );
}
