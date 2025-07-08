import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import PredictForm from './PredictForm';
import './App.css';
import About from './pages/About';
import Home from './pages/Home';
import { useEffect } from 'react';

function App() {
  useEffect(() => {
    document.title = "PredictorFC";
  }, []);
  return (
    <Router>
      <div className="min-h-screen bg-gradient-to-br from-blue-100 to-white flex flex-col">
        {/* Navbar */}
        <nav className="bg-white shadow-md px-6 py-4 flex justify-between items-center">
          <div className="flex items-center space-x-6">
            <img
              src="/PredictorFCLogo.png"
              alt="Predictor FC Logo"
              className="h-20 w-auto"
            />
            <div className="hidden md:flex space-x-4 text-gray-700 font-semibold">
              <Link to="/" className="hover:text-blue-600">Home</Link>
              <Link to="/predict" className="hover:text-blue-600">Predict</Link>
              <Link to="/about" className="hover:text-blue-600">About</Link>
            </div>
          </div>
          <div className="text-sm text-gray-500">Built with Django + React</div>
        </nav>

        {/* Main Content */}
        <main className="flex-grow">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/predict" element={<PredictForm />} />
            <Route path="/about" element={<About />} />
          </Routes>
        </main>

        {/* Footer */}
        <footer className="text-center text-sm text-gray-400 py-2">
          © 2025 Predictor FC. Built by Christian Rodriguez.
        </footer>
      </div>
    </Router>
  );
}

export default App;