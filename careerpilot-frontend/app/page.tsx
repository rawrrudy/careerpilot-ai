export default function Home() {
  return (
    <main className="min-h-screen bg-black text-white flex items-center justify-center">
      <div className="text-center">
        <h1 className="text-6xl font-bold mb-6">
          CareerPilotAI
        </h1>

        <p className="text-gray-400 text-xl mb-8">
          Your AI-Powered Career Guidance Platform
        </p>

        <button className="bg-white text-black px-6 py-3 rounded-xl font-semibold hover:scale-105 transition">
          Get Started
        </button>
      </div>
    </main>
  );
}