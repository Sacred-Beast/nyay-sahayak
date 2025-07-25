import React, { useState } from "react";
import { analyzeCase, factCheck } from "../api";

function QueryForm({ caseId, onResult, onFactCheck }) {
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    setLoading(true);
    try {
      const res = await analyzeCase(caseId, query);
      onResult(res.data.argument);
      const fc = await factCheck(caseId, res.data.argument);
      onFactCheck(fc.data.fact_check);
    } catch (e) {
      alert("Analysis failed");
    }
    setLoading(false);
  };

  return (
    <div className="mb-6 w-full max-w-xl">
      <textarea
        className="w-full border rounded p-2 mb-2"
        rows={3}
        placeholder="Enter your legal query..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button
        onClick={handleAnalyze}
        disabled={!query || loading}
        className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
      >
        {loading ? "Analyzing..." : "Analyze"}
      </button>
    </div>
  );
}

export default QueryForm;
