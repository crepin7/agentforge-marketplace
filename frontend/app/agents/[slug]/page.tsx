"use client";
import { useQuery } from "@tanstack/react-query";
import { useParams } from "next/navigation";

export default function AgentPage() {
  const { slug } = useParams<{ slug: string }>();
  const { data, isLoading, error } = useQuery({
    queryKey: ["agent", slug],
    queryFn: async () => {
      const r = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/v1/agents/${slug}`);
      if (!r.ok) throw new Error("Agent introuvable");
      return r.json();
    },
  });

  if (isLoading) return <main className="p-12 text-slate-300">Chargement…</main>;
  if (error) return <main className="p-12 text-red-400">Erreur de chargement.</main>;

  return (
    <main className="mx-auto max-w-4xl px-6 py-16">
      <p className="text-sm text-slate-400">Agent</p>
      <h1 className="mt-2 text-4xl font-bold">{data.name}</h1>
      <p className="mt-3 text-lg text-slate-300">{data.tagline}</p>
      <div className="mt-8 flex flex-wrap gap-2">
        {data.tags?.map((t: string) => (
          <span key={t} className="rounded-md bg-slate-800 px-2 py-0.5 text-xs text-slate-300">{t}</span>
        ))}
      </div>
      <div className="mt-10 rounded-xl border border-slate-800 bg-slate-900/50 p-6">
        <h2 className="text-lg font-semibold">Pricing</h2>
        <p className="mt-1 text-2xl font-bold text-forge-500">{(data.pricing?.price_cents / 100).toFixed(2)}$/mois</p>
      </div>
    </main>
  );
}
