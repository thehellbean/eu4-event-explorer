import { createStore, applyMiddleware } from "redux";
import thunk from 'redux-thunk';
import rootReducer from "../reducers";
import { initialState } from "../reducers"

export default function configureStore(initial=initialState) {
	return createStore(
		rootReducer,
		initial,
		applyMiddleware(thunk)
		)
}