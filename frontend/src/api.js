import axios from "axios";

const API_BASE = process.env.REACT_APP_API_URL || "http://localhost:8000";

export const uploadDocument = (file) => {
  const formData = new FormData();
  formData.append("file", file);
  return axios.post(`${API_BASE}/upload`, formData);
};

export const analyzeCase = (case_id, user_query) => {
  const formData = new FormData();
  formData.append("case_id", case_id);
  formData.append("user_query", user_query);
  return axios.post(`${API_BASE}/analyze`, formData);
};

export const factCheck = (case_id, argument) => {
  const formData = new FormData();
  formData.append("case_id", case_id);
  formData.append("argument", argument);
  return axios.post(`${API_BASE}/fact-check`, formData);
};

export const fetchGraph = (case_id) => {
  return axios.get(`${API_BASE}/graph/${case_id}`);
};
