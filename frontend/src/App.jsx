import React, { useState } from "react";
import FileUpload from "./components/FileUpload";
import QueryForm from "./components/QueryForm";
import ResultsView from "./components/ResultsView";
import GraphVisualizer from "./components/GraphVisualizer";

function App() {
  const [caseId, setCaseId] = useState(null);
  const [argument, setArgument] = useState(null);
  const [factCheck, setFactCheck] = useState(null);

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center p-6">
      <h1 className="text-3xl font-bold mb-6 text-blue-800">Nyay-Sahayak</h1>
      <FileUpload onUpload={setCaseId} />
      {caseId && (
        <QueryForm
          caseId={caseId}
          onResult={(arg) => setArgument(arg)}
          onFactCheck={setFactCheck}
        />
      )}
      {argument && factCheck && (
        <ResultsView argument={argument} factCheck={factCheck} />
      )}
      {caseId && <GraphVisualizer caseId={caseId} />}
    </div>
  );
}

export default App;
