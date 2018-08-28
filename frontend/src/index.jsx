import React from 'react';
import { render } from 'react-dom';
import { Provider } from "react-redux";
import configureStore from "./js/store/index";

import EventList from "./js/components/EventList.jsx"
import App from './js/components/App.jsx';

const store = configureStore();

render(
	<Provider store={store}>
		<App/>
	</Provider>,
	document.getElementById("app")
	)