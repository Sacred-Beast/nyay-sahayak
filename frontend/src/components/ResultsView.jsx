import React from "react";
import FactCheckSentence from "./FactCheckSentence";

function ResultsView({ argument, factCheck }) {
  // Split argument into sentences and match with factCheck
  return (
    <div className="bg-white shadow rounded p-6 w-full max-w-3xl mb-8">
      <h2 className="text-xl font-semibold mb-4">Fact-Checked Argument</h2>
      {factCheck.map((fc, idx) => (
        <FactCheckSentence key={idx} {...fc} />
      ))}
    </div>
  );
}

export default ResultsView;
