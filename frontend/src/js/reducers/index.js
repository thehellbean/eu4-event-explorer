import { combineReducers } from 'redux';
import { events, eventsIsLoading, eventsHasErrored } from './items';

export const initialState = {
	events: [],
	eventsHasErrored: false,
	eventsIsLoading: false
};

export default combineReducers({
	events,
	eventsHasErrored,
	eventsIsLoading
});