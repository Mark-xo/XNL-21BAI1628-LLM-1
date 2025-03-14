import React from "react";
import { Provider, useSelector } from "react-redux";
import { store } from "./app/store";
import Login from "./components/Login";
import Dashboard from "./components/Dashboard";
import { RootState } from "./app/store";

const App: React.FC = () => {
  const token = useSelector((state: RootState) => state.user.token);
  return (
    <>
      {token ? <Dashboard /> : <Login />}
    </>
  );
};

const AppWrapper: React.FC = () => (
  <Provider store={store}>
    <App />
  </Provider>
);

export default AppWrapper;