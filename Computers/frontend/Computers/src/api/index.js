import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000/api/computers'

export function getComputers() {
  return axios.get(`${API_URL}`)
}

export function getComputer(computerid) {
  return axios.get(`${API_URL}/${computerid}`)
}

export function deleteComputer(computerid) {
  return axios.delete(`${API_URL}/${computerid}`)
}

export function putComputer(computerid, computer) {
  return axios.put(`${API_URL}/${computerid}`, {...computer})
}

export function postComputer(computer) {
  return axios.post(`${API_URL}`, {...computer})
}


