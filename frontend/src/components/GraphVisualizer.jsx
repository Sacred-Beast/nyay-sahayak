import React, { useEffect, useRef, useState } from "react";
import ForceGraph2D from "react-force-graph-2d";
import { fetchGraph } from "../api";

function GraphVisualizer({ caseId }) {
  const [graph, setGraph] = useState({ nodes: [], edges: [] });

  useEffect(() => {
    fetchGraph(caseId).then((res) => setGraph({
      nodes: res.data.nodes,
      links: res.data.edges.map(e => ({
        source: e.source,
        target: e.target,
        label: e.type
      }))
    }));
  }, [caseId]);

  return (
    <div className="bg-white shadow rounded p-6 w-full max-w-3xl mb-8">
      <h2 className="text-xl font-semibold mb-4">Knowledge Graph</h2>
      <div style={{ height: 400 }}>
        <ForceGraph2D
          graphData={graph}
          nodeLabel="label"
          linkLabel="label"
          nodeAutoColorBy="label"
        />
      </div>
    </div>
  );
}

export default GraphVisualizer;
