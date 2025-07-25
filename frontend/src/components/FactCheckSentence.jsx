import React from "react";

function FactCheckSentence({ sentence, status, supporting_text, similarity }) {
  return (
    <div className="flex items-start mb-2">
      <span className="mr-2">
        {status === "Verified" ? (
          <span title="Verified" className="text-green-600">✔️</span>
        ) : (
          <span title="Needs Review" className="text-red-600">⚠️</span>
        )}
      </span>
      <div>
        <span className="font-medium">{sentence}</span>
        <div className="text-xs text-gray-500">
          <span>
            {status} (Similarity: {similarity})<br />
            <span className="italic">Source: {supporting_text}</span>
          </span>
        </div>
      </div>
    </div>
  );
}

export default FactCheckSentence;
