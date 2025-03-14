import { configureStore } from '@reduxjs/toolkit';
import userReducer from 'C:/Something New/programs/XNL-21BAI1628-LLM-1/frontend/src/features/user/userSlice';

export const store = configureStore({
  reducer: {
    user: userReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
