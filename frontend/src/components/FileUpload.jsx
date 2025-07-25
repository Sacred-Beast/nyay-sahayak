import React, { useState } from "react";
import { uploadDocument } from "../api";

function FileUpload({ onUpload }) {
  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);

  const handleChange = (e) => setFile(e.target.files[0]);

  const handleUpload = async () => {
    setUploading(true);
    try {
      const res = await uploadDocument(file);
      onUpload(res.data.case_id);
    } catch (e) {
      alert("Upload failed");
    }
    setUploading(false);
  };

  return (
    <div className="mb-6">
      <input
        type="file"
        accept=".pdf"
        onChange={handleChange}
        className="mb-2"
      />
      <button
        onClick={handleUpload}
        disabled={!file || uploading}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        {uploading ? "Uploading..." : "Upload Case Document"}
      </button>
    </div>
  );
}

export default FileUpload;
