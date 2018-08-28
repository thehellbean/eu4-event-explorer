import { combineReducers } from 'redux';
import { events, eventsIsLoading, eventsHasErrored } from './items';

export default combineReducers({
	events,
	eventsHasErrored,
	eventsIsLoading
});