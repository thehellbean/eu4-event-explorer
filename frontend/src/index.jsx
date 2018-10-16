import React from 'react';
import { render } from 'react-dom';
import { Provider } from "react-redux";
import configureStore from "./js/store/index.js";

import EventList from "./js/components/EventList.jsx"
import Event from "./js/components/Event.jsx"
import App from './js/components/App.jsx';
import { eventsFetchData } from './js/actions/items.js';

const store = configureStore();

store.dispatch(eventsFetchData("http://localhost:8080/api/search", {}));

render(
	<Provider store={store}>
		<App/>
	</Provider>,
	document.getElementById("app")
	)