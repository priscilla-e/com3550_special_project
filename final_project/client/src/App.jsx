import {useContext} from "react";
import GameContext from "./contexts/game-context.jsx";
import Header from './components/layout/Header.jsx';
import Footer from "./components/layout/Footer.jsx";
import ModePage from './pages/ModePage.jsx';
import SettingsPage from "./pages/SettingsPage.jsx";
import GamePage from "./pages/GamePage.jsx"
import { ToastContainer } from "react-toastify";

function App() {
    const ctx = useContext(GameContext)

    return (
        <>
            <Header/>
            <main className="container mx-auto px-2 ">
                {ctx.page === 0 && <ModePage/>}
                {ctx.page === 1 && <SettingsPage/>}
                {ctx.page === 2 && <GamePage />}
            </main>
            <Footer/>
            <ToastContainer theme="dark"/>
        </>
    );
}

export default App;
