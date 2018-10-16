import { EVENTS_HAS_ERRORED, EVENTS_IS_LOADING, EVENTS_FETCH_DATA_SUCCESS, EVENTS_FINISHED_LOADING } from "../constants/action-types";
import { initialState } from "./index.js"

export function eventsHasErrored(state = false, action) {
	switch(action.type) {
		case EVENTS_HAS_ERRORED:
			return action.hasErrored;

		default:
			return state;
	}
}

export function eventsIsLoading(state = false, action) {
	switch(action.type) {
		case EVENTS_IS_LOADING:
			return action.isLoading;

		default:
			return state;
	}
}

export function events(state = [], action) {
	switch(action.type) {
		case EVENTS_FETCH_DATA_SUCCESS:
			return action.events;

		default:
			return state;
	}
}